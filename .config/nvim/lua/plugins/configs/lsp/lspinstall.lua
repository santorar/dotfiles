require("nvim-lsp-installer").setup{
    automatic_installation = true,
    ensure_installed = {"sumeko_lua"},
    ui = {
        icons = {
            server_installed = "✓",
            server_pending = "➜",
            server_uninstalled = "✗"
        }
    },
      keymaps = {
         toggle_server_expand = "<CR>",
         install_server = "i",
         update_server = "u",
         check_server_version = "c",
         update_all_servers = "U",
         check_outdated_servers = "C",
         uninstall_server = "X",
      },
}
